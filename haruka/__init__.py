
    try:
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    except ValueError:
        raise Exception("Your sudo users list does not contain valid integers.")

    try:
        SUPPORT_USERS = set(int(x) for x in os.environ.get("SUPPORT_USERS", "").split())
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WHITELIST_USERS = set(int(x) for x in os.environ.get("WHITELIST_USERS", "").split())
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    WEBHOOK = bool(os.environ.get('WEBHOOK', False))
    URL = os.environ.get('URL', "")  # Does not contain token
    PORT = int(os.environ.get('PORT', 5432))
    CERT_PATH = os.environ.get("CERT_PATH")

    DB_URI = os.environ.get('DATABASE_URL')
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    DEL_CMDS = bool(os.environ.get('DEL_CMDS', False))
    STRICT_ANTISPAM = bool(os.environ.get('STRICT_ANTISPAM', False))
    WORKERS = int(os.environ.get('WORKERS', 8))
    BAN_STICKER = os.environ.get('BAN_STICKER', 'CAADAgADEAgAAgi3GQL9YQyT_kBpQwI')
    ALLOW_EXCL = os.environ.get('ALLOW_EXCL', False)
    API_WEATHER = os.environ.get('API_OPENWEATHER', None)

else:
    from haruka.config import Development as Config
    TOKEN = Config.API_KEY
    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    MESSAGE_DUMP = Config.MESSAGE_DUMP
    OWNER_USERNAME = Config.OWNER_USERNAME

    try:
        SUDO_USERS = set(int(x) for x in Config.SUDO_USERS or [])
    except ValueError:
        raise Exception("Your sudo users list does not contain valid integers.")

    
        raise Exception("Your whitelisted users list does not contain valid integers.")

    PENWEATHER) 


SUDO_USERS.add(OWNER_ID)

updater = tg.Updater(TOKEN, workers=WORKERS)

dispatcher = updater.dispatcher

SUDO_USERS = list(SUDO_USERS)
