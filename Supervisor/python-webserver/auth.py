import bcrypt
import base64
import hashlib

from datetime import datetime, timedelta
from time import time


password = b"an incredibly long password" * 10
pw = base64.b64encode(hashlib.sha256(password).digest())
hashed = bcrypt.hashpw(
	pw,
	bcrypt.gensalt()
)

bcrypt.checkpw(pw, hashed)
