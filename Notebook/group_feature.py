"""
group_feature.py

Manual feature grouping helper for the Home Credit Default Risk dataset.

Purpose:
- Keep notebook clean.
- Use the official HomeCredit_columns_description.csv file.
- Create file-wise feature group reports.
- Create compact summaries for schema understanding before EDA.

Main function to use in notebook:
    create_feature_group_reports(description_path, output_dir, data=None)
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional, Any

import pandas as pd


ENCODING_CANDIDATES = ("utf-8", "utf-8-sig", "cp1252", "latin1")


TABLE_NAME_MAP = {
    "application_{train|test}.csv": "application",
    "application_train.csv": "application",
    "application_test.csv": "application",
    "bureau.csv": "bureau",
    "bureau_balance.csv": "bureau_balance",
    "previous_application.csv": "previous_application",
    "POS_CASH_balance.csv": "pos_cash_balance",
    "pos_cash_balance.csv": "pos_cash_balance",
    "installments_payments.csv": "installments_payments",
    "credit_card_balance.csv": "credit_card_balance",
}


DATA_KEY_TO_DESCRIPTION_TABLE = {
    "application_train": "application",
    "application_test": "application",
    "bureau": "bureau",
    "bureau_balance": "bureau_balance",
    "previous_application": "previous_application",
    "pos_cash_balance": "pos_cash_balance",
    "POS_CASH_balance": "pos_cash_balance",
    "installments_payments": "installments_payments",
    "credit_card_balance": "credit_card_balance",
}


COLUMN_NAME_FIXES = {
    "SK_BUREAU_ID": "SK_ID_BUREAU",
    "SK_ID_PREV ": "SK_ID_PREV",
}


def _read_csv_with_fallback(path: Path) -> pd.DataFrame:
    """Read CSV using a small encoding fallback list."""
    last_error = None

    for encoding in ENCODING_CANDIDATES:
        try:
            return pd.read_csv(path, encoding=encoding)
        except UnicodeDecodeError as error:
            last_error = error

    raise UnicodeDecodeError(
        "unknown",
        b"",
        0,
        1,
        f"Could not read {path} using {ENCODING_CANDIDATES}. Last error: {last_error}",
    )


def normalize_table_name(table_name: Any) -> str:
    """Normalize official description table names to project table keys."""
    if pd.isna(table_name):
        return "unknown_table"

    table = str(table_name).strip()
    return TABLE_NAME_MAP.get(table, table.replace(".csv", "").strip().lower())


def normalize_column_name(column_name: Any) -> str:
    """Normalize known column naming issues in the description file."""
    if pd.isna(column_name):
        return "unknown_column"

    col = str(column_name).strip()
    return COLUMN_NAME_FIXES.get(col, col)


def load_column_description(description_path: Path | str) -> pd.DataFrame:
    """Load and normalize HomeCredit_columns_description.csv."""
    description_path = Path(description_path)
    desc = _read_csv_with_fallback(description_path)

    rename_map = {
        "Table": "source_table_raw",
        "Row": "column_name_raw",
        "Description": "description",
        "Special": "special",
    }

    desc = desc.rename(columns={k: v for k, v in rename_map.items() if k in desc.columns})

    required_cols = {"source_table_raw", "column_name_raw", "description"}
    missing_cols = required_cols - set(desc.columns)

    if missing_cols:
        raise ValueError(f"Column description file is missing required columns: {sorted(missing_cols)}")

    desc["source_table_raw"] = desc["source_table_raw"].astype(str).str.strip()
    desc["source_table"] = desc["source_table_raw"].apply(normalize_table_name)
    desc["column_name"] = desc["column_name_raw"].apply(normalize_column_name)
    desc["description"] = desc["description"].fillna("").astype(str).str.strip()

    if "special" not in desc.columns:
        desc["special"] = ""
    else:
        desc["special"] = desc["special"].fillna("").astype(str).str.strip()

    return desc


def assign_feature_group(source_table: str, column_name: str, description: str = "") -> str:
    """Assign a manually curated feature group using table context and column meaning."""
    table = normalize_table_name(source_table)
    col = normalize_column_name(column_name).upper()

    # Universal keys and target
    if col in {"SK_ID_CURR", "SK_ID_PREV", "SK_ID_BUREAU"}:
        return "id_key"

    if col == "TARGET":
        return "target"

    # Application table
    if table == "application":
        if col in {
            "NAME_CONTRACT_TYPE",
            "CODE_GENDER",
            "NAME_TYPE_SUITE",
            "NAME_INCOME_TYPE",
            "NAME_EDUCATION_TYPE",
            "NAME_FAMILY_STATUS",
            "NAME_HOUSING_TYPE",
            "OCCUPATION_TYPE",
            "ORGANIZATION_TYPE",
            "WEEKDAY_APPR_PROCESS_START",
        }:
            return "applicant_profile_category"

        if col in {"CNT_CHILDREN", "CNT_FAM_MEMBERS"}:
            return "family_count"

        if col.startswith("AMT_"):
            return "financial_amount"

        if col.startswith("DAYS_") or col == "OWN_CAR_AGE":
            return "time_days_age"

        if col.startswith("FLAG_DOCUMENT"):
            return "document_flag"

        if col in {
            "FLAG_MOBIL",
            "FLAG_EMP_PHONE",
            "FLAG_WORK_PHONE",
            "FLAG_CONT_MOBILE",
            "FLAG_PHONE",
            "FLAG_EMAIL",
        }:
            return "contact_flag"

        if col in {"FLAG_OWN_CAR", "FLAG_OWN_REALTY"} or col.startswith("FLAG_"):
            return "binary_flag"

        if (
            col.startswith("REGION_")
            or col.startswith("REG_REGION")
            or col.startswith("REG_CITY")
            or col.startswith("LIVE_CITY")
            or col.startswith("LIVE_REGION")
        ):
            return "region_location"

        if col == "HOUR_APPR_PROCESS_START":
            return "time_hour"

        if col.startswith("EXT_SOURCE"):
            return "external_score"

        if col.startswith("OBS_") or col.startswith("DEF_"):
            return "social_circle"

        if col.startswith("AMT_REQ_CREDIT_BUREAU"):
            return "bureau_request_count"

        if col in {
            "FONDKAPREMONT_MODE",
            "HOUSETYPE_MODE",
            "WALLSMATERIAL_MODE",
            "EMERGENCYSTATE_MODE",
        }:
            return "housing_category"

        building_tokens = (
            "APARTMENTS",
            "BASEMENTAREA",
            "YEARS_BEGINEXPLUATATION",
            "YEARS_BUILD",
            "COMMONAREA",
            "ELEVATORS",
            "ENTRANCES",
            "FLOORSMAX",
            "FLOORSMIN",
            "LANDAREA",
            "LIVINGAPARTMENTS",
            "LIVINGAREA",
            "NONLIVINGAPARTMENTS",
            "NONLIVINGAREA",
            "TOTALAREA",
        )

        if any(token in col for token in building_tokens):
            return "building_housing_numeric"

    # Bureau table
    if table == "bureau":
        if col in {"CREDIT_ACTIVE", "CREDIT_CURRENCY", "CREDIT_TYPE"}:
            return "bureau_credit_category"

        if col.startswith("DAYS_"):
            return "bureau_time_days"

        if col in {"AMT_CREDIT_SUM", "AMT_CREDIT_SUM_LIMIT", "AMT_ANNUITY"}:
            return "bureau_credit_amount"

        if col in {
            "AMT_CREDIT_SUM_DEBT",
            "AMT_CREDIT_SUM_OVERDUE",
            "AMT_CREDIT_MAX_OVERDUE",
            "CREDIT_DAY_OVERDUE",
        }:
            return "bureau_debt_overdue"

        if col == "CNT_CREDIT_PROLONG":
            return "bureau_prolong_count"

    # Bureau balance table
    if table == "bureau_balance":
        if col == "MONTHS_BALANCE":
            return "time_months"

        if col == "STATUS":
            return "bureau_balance_status"

    # Previous application table
    if table == "previous_application":
        if col.startswith("AMT_"):
            return "previous_application_amount"

        if col.startswith("DAYS_"):
            return "previous_application_time_days"

        if col.startswith("RATE_"):
            return "previous_application_rate"

        if col.startswith("NFLAG_") or col.startswith("FLAG_"):
            return "previous_application_flag"

        if col == "CNT_PAYMENT":
            return "previous_application_count"

        if col == "HOUR_APPR_PROCESS_START":
            return "time_hour"

        if col == "SELLERPLACE_AREA":
            return "seller_area"

        if (
            col.startswith("NAME_")
            or col.startswith("CODE_")
            or col in {"CHANNEL_TYPE", "PRODUCT_COMBINATION", "WEEKDAY_APPR_PROCESS_START"}
        ):
            return "previous_application_category"

    # POS cash monthly balance
    if table == "pos_cash_balance":
        if col == "MONTHS_BALANCE":
            return "time_months"

        if col in {"CNT_INSTALMENT", "CNT_INSTALMENT_FUTURE"}:
            return "pos_installment_count"

        if col == "NAME_CONTRACT_STATUS":
            return "contract_status"

        if col in {"SK_DPD", "SK_DPD_DEF"}:
            return "delinquency_dpd"

    # Installments payments
    if table == "installments_payments":
        if col.startswith("NUM_INSTALMENT"):
            return "installment_number"

        if col.startswith("DAYS_"):
            return "installment_time_days"

        if col.startswith("AMT_"):
            return "installment_payment_amount"

    # Credit card balance
    if table == "credit_card_balance":
        if col == "MONTHS_BALANCE":
            return "time_months"

        if col == "NAME_CONTRACT_STATUS":
            return "contract_status"

        if col in {"SK_DPD", "SK_DPD_DEF"}:
            return "delinquency_dpd"

        if "DRAWINGS" in col:
            return "credit_card_drawings"

        if "PAYMENT" in col or "INST_MIN" in col:
            return "credit_card_payment"

        if "RECEIVABLE" in col or "RECIVABLE" in col:
            return "credit_card_receivable"

        if "BALANCE" in col or "LIMIT" in col:
            return "credit_card_balance_limit"

        if col.startswith("CNT_"):
            return "credit_card_count"

        if col.startswith("AMT_"):
            return "credit_card_amount"

    # Generic fallback groups
    if col.startswith("AMT_"):
        return "financial_amount"

    if col.startswith("DAYS_"):
        return "time_days"

    if col.startswith("MONTHS_"):
        return "time_months"

    if col.startswith("CNT_"):
        return "count_feature"

    if col.startswith("FLAG_") or col.startswith("NFLAG_"):
        return "binary_flag"

    if col.startswith("NAME_") or col.startswith("CODE_"):
        return "categorical_feature"

    if "STATUS" in col:
        return "status_category"

    if "DPD" in col or "OVERDUE" in col:
        return "delinquency_risk"

    if "PAYMENT" in col or "INSTALMENT" in col:
        return "payment_installment"

    if "CREDIT" in col or "ANNUITY" in col:
        return "credit_related"

    return "other"


def semantic_is_categorical(feature_group: str) -> bool:
    """Return True if feature group should usually be treated as categorical."""
    return (
        "category" in feature_group
        or feature_group
        in {
            "contract_status",
            "bureau_balance_status",
            "housing_category",
            "applicant_profile_category",
            "previous_application_category",
            "bureau_credit_category",
        }
    )


def assign_semantic_type(feature_group: str, column_name: str) -> str:
    """Map feature group to broad semantic type."""
    col = normalize_column_name(column_name).upper()

    if feature_group == "id_key":
        return "identifier"

    if feature_group == "target":
        return "target"

    if semantic_is_categorical(feature_group):
        return "categorical"

    if "flag" in feature_group:
        return "binary_flag"

    if "time" in feature_group or "days" in feature_group or "months" in feature_group or col.startswith("DAYS_"):
        return "time_offset"

    if (
        "amount" in feature_group
        or "balance" in feature_group
        or "receivable" in feature_group
        or "drawings" in feature_group
        or "financial" in feature_group
    ):
        return "numeric_amount"

    if "count" in feature_group or col.startswith("CNT_") or col.startswith("NUM_"):
        return "numeric_count"

    if "rate" in feature_group or "score" in feature_group or "ratio" in feature_group:
        return "numeric_ratio_score"

    if "dpd" in feature_group or "overdue" in feature_group or "delinquency" in feature_group:
        return "risk_numeric"

    return "numeric_or_other"


def assign_aggregation_hint(source_table: str, feature_group: str, column_name: str) -> str:
    """Suggest safe future aggregation handling."""
    table = normalize_table_name(source_table)

    if feature_group == "id_key":
        return "merge_key_only"

    if feature_group == "target":
        return "target_only_train"

    if table == "application":
        return "keep_or_engineer_application_level"

    if table == "bureau_balance":
        if feature_group == "bureau_balance_status":
            return "count_frequency_by_SK_ID_BUREAU_then_SK_ID_CURR"
        return "aggregate_by_SK_ID_BUREAU_then_SK_ID_CURR"

    if table in {"pos_cash_balance", "credit_card_balance"}:
        if semantic_is_categorical(feature_group):
            return "count_frequency_by_SK_ID_PREV_then_SK_ID_CURR"
        return "aggregate_by_SK_ID_PREV_then_SK_ID_CURR"

    if table == "installments_payments":
        return "derive_payment_behavior_then_aggregate_by_SK_ID_PREV_then_SK_ID_CURR"

    if table == "previous_application":
        if semantic_is_categorical(feature_group):
            return "count_frequency_by_SK_ID_CURR"
        return "aggregate_by_SK_ID_CURR"

    if table == "bureau":
        if semantic_is_categorical(feature_group):
            return "count_frequency_by_SK_ID_CURR"
        return "aggregate_by_SK_ID_CURR"

    return "review_before_use"


def build_feature_group_table(description_path: Path | str) -> pd.DataFrame:
    """Build the full feature group catalogue from the official column description file."""
    desc = load_column_description(description_path)

    catalog = desc.copy()

    catalog["feature_group"] = catalog.apply(
        lambda row: assign_feature_group(
            row["source_table"],
            row["column_name"],
            row["description"],
        ),
        axis=1,
    )

    catalog["semantic_type"] = catalog.apply(
        lambda row: assign_semantic_type(
            row["feature_group"],
            row["column_name"],
        ),
        axis=1,
    )

    catalog["aggregation_hint"] = catalog.apply(
        lambda row: assign_aggregation_hint(
            row["source_table"],
            row["feature_group"],
            row["column_name"],
        ),
        axis=1,
    )

    keep_cols = [
        "source_table_raw",
        "source_table",
        "column_name_raw",
        "column_name",
        "feature_group",
        "semantic_type",
        "aggregation_hint",
        "description",
        "special",
    ]

    return (
        catalog[keep_cols]
        .sort_values(["source_table", "feature_group", "column_name"])
        .reset_index(drop=True)
    )


def summarize_feature_groups(feature_group_catalog: pd.DataFrame) -> pd.DataFrame:
    """Create long table: source table x feature group counts."""
    return (
        feature_group_catalog
        .groupby(["source_table", "feature_group"], dropna=False)
        .size()
        .reset_index(name="column_count")
        .sort_values(
            ["source_table", "column_count", "feature_group"],
            ascending=[True, False, True],
        )
        .reset_index(drop=True)
    )


def pivot_feature_groups(feature_group_catalog: pd.DataFrame) -> pd.DataFrame:
    """Create wide pivot table: one row per source table, one column per feature group."""
    return (
        summarize_feature_groups(feature_group_catalog)
        .pivot_table(
            index="source_table",
            columns="feature_group",
            values="column_count",
            fill_value=0,
        )
        .reset_index()
    )


def create_table_overview(feature_group_catalog: pd.DataFrame) -> pd.DataFrame:
    """Create compact table-level overview."""
    records = []

    for table_name, group in feature_group_catalog.groupby("source_table"):
        records.append(
            {
                "source_table": table_name,
                "total_columns_in_description": len(group),
                "feature_group_count": group["feature_group"].nunique(),
                "id_columns": ", ".join(
                    group.loc[group["semantic_type"] == "identifier", "column_name"].tolist()
                )
                or "None",
                "has_target": bool((group["semantic_type"] == "target").any()),
                "categorical_columns": int((group["semantic_type"] == "categorical").sum()),
                "numeric_amount_columns": int((group["semantic_type"] == "numeric_amount").sum()),
                "time_offset_columns": int((group["semantic_type"] == "time_offset").sum()),
                "binary_flag_columns": int((group["semantic_type"] == "binary_flag").sum()),
                "count_columns": int((group["semantic_type"] == "numeric_count").sum()),
            }
        )

    return pd.DataFrame(records).sort_values("source_table").reset_index(drop=True)


def validate_grouping(feature_group_catalog: pd.DataFrame) -> pd.DataFrame:
    """Validate grouping quality from the description file."""
    total_columns = len(feature_group_catalog)
    other_count = int((feature_group_catalog["feature_group"] == "other").sum())
    missing_group_count = int(feature_group_catalog["feature_group"].isna().sum())

    return pd.DataFrame(
        [
            {
                "check_name": "total_columns_in_description",
                "value": total_columns,
                "status": "info",
            },
            {
                "check_name": "columns_with_missing_group",
                "value": missing_group_count,
                "status": "pass" if missing_group_count == 0 else "review",
            },
            {
                "check_name": "columns_assigned_to_other",
                "value": other_count,
                "status": "pass" if other_count == 0 else "review",
            },
            {
                "check_name": "unique_source_tables",
                "value": feature_group_catalog["source_table"].nunique(),
                "status": "info",
            },
            {
                "check_name": "unique_feature_groups",
                "value": feature_group_catalog["feature_group"].nunique(),
                "status": "info",
            },
        ]
    )


def validate_feature_groups_against_data(
    data: Dict[str, Optional[pd.DataFrame]],
    feature_group_catalog: pd.DataFrame,
) -> pd.DataFrame:
    """Compare loaded dataframe columns against the description-based feature catalogue."""
    records = []

    for data_key, df in data.items():
        if df is None:
            records.append(
                {
                    "data_key": data_key,
                    "description_table": DATA_KEY_TO_DESCRIPTION_TABLE.get(data_key, "unknown"),
                    "loaded": False,
                    "actual_columns": 0,
                    "description_columns": 0,
                    "missing_in_data_count": None,
                    "extra_in_data_count": None,
                    "missing_in_data": "not_loaded",
                    "extra_in_data": "not_loaded",
                    "status": "not_loaded",
                }
            )
            continue

        desc_table = DATA_KEY_TO_DESCRIPTION_TABLE.get(data_key, data_key)
        desc_cols = set(
            feature_group_catalog.loc[
                feature_group_catalog["source_table"] == desc_table,
                "column_name",
            ]
        )

        actual_cols = {normalize_column_name(col) for col in df.columns}

        missing_in_data = sorted(desc_cols - actual_cols)
        extra_in_data = sorted(actual_cols - desc_cols)

        # TARGET is expected in application_train but not application_test.
        if data_key == "application_test" and "TARGET" in missing_in_data:
            missing_in_data.remove("TARGET")

        status = "pass" if len(missing_in_data) == 0 and len(extra_in_data) == 0 else "review"

        records.append(
            {
                "data_key": data_key,
                "description_table": desc_table,
                "loaded": True,
                "actual_columns": len(actual_cols),
                "description_columns": len(desc_cols),
                "missing_in_data_count": len(missing_in_data),
                "extra_in_data_count": len(extra_in_data),
                "missing_in_data": ", ".join(missing_in_data) if missing_in_data else "None",
                "extra_in_data": ", ".join(extra_in_data) if extra_in_data else "None",
                "status": status,
            }
        )

    return pd.DataFrame(records)


def create_feature_group_reports(
    description_path: Path | str,
    output_dir: Optional[Path | str] = None,
    data: Optional[Dict[str, Optional[pd.DataFrame]]] = None,
) -> Dict[str, pd.DataFrame]:
    """
    Create all feature group reports.

    Parameters
    ----------
    description_path:
        Path to HomeCredit_columns_description.csv.

    output_dir:
        Directory to save report CSV files. If None, files are not saved.

    data:
        Optional dictionary of loaded dataframes from notebook.

    Returns
    -------
    dict of pandas DataFrames:
        catalog, summary, pivot, table_overview, grouping_validation,
        and optionally data_validation.
    """
    catalog = build_feature_group_table(description_path)
    summary = summarize_feature_groups(catalog)
    pivot = pivot_feature_groups(catalog)
    table_overview = create_table_overview(catalog)
    grouping_validation = validate_grouping(catalog)

    reports = {
        "catalog": catalog,
        "summary": summary,
        "pivot": pivot,
        "table_overview": table_overview,
        "grouping_validation": grouping_validation,
    }

    if data is not None:
        reports["data_validation"] = validate_feature_groups_against_data(data, catalog)

    if output_dir is not None:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        catalog.to_csv(output_dir / "feature_group_catalog.csv", index=False)
        summary.to_csv(output_dir / "feature_group_summary_by_table.csv", index=False)
        pivot.to_csv(output_dir / "feature_group_pivot_by_table.csv", index=False)
        table_overview.to_csv(output_dir / "feature_group_table_overview.csv", index=False)
        grouping_validation.to_csv(output_dir / "feature_grouping_validation.csv", index=False)

        if "data_validation" in reports:
            reports["data_validation"].to_csv(
                output_dir / "feature_group_data_validation.csv",
                index=False,
            )

    return reports


__all__ = [
    "load_column_description",
    "build_feature_group_table",
    "summarize_feature_groups",
    "pivot_feature_groups",
    "create_table_overview",
    "validate_grouping",
    "validate_feature_groups_against_data",
    "create_feature_group_reports",
]