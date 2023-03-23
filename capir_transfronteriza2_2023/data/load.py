from pathlib import Path, PosixPath
from typing import Union
import pandas as pd
import capir_transfronteriza2_2023.utils.paths as paths


# Inputs
data_raw = paths.data_raw_dir()
data_processed = paths.data_processed_dir()
data_urls = paths.data_urls_dir()
data_ids = paths.data_ids_dir()
data_jsonl = paths.data_jsonl_dir()
data_minet = paths.data_minet_dir()


# Outputs
users = paths.data_raw_dir("users.csv")

