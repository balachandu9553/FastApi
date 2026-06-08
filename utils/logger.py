import logging
import os

# -------------------------------
# Create logs folder
# -------------------------------
if not os.path.exists("logs"):
    os.makedirs("logs")

# -------------------------------
# Create logger
# -------------------------------
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# -------------------------------
# Formatter (IMPORTANT)
# -------------------------------
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s - line:%(lineno)d - %(message)s"
)

# -------------------------------
# INFO file
# -------------------------------
info_handler = logging.FileHandler("logs/info.log")
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

# -------------------------------
# WARNING file
# -------------------------------
warning_handler = logging.FileHandler("logs/warning.log")
warning_handler.setLevel(logging.WARNING)
warning_handler.setFormatter(formatter)

# -------------------------------
# ERROR file
# -------------------------------
error_handler = logging.FileHandler("logs/error.log")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

# -------------------------------
# Add handlers
# -------------------------------
logger.addHandler(info_handler)
logger.addHandler(warning_handler)
logger.addHandler(error_handler)