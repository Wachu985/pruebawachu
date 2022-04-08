import os


class Config:
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    Token = os.environ.get("BOT_TOKEN")
    Session = os.environ.get("Session_String")
    if Session is None or Session == "":
        Session = ":memory:"
    App_Name = os.environ.get("APP_NAME")
    Port = int(os.environ.get("PORT"))
    Archive_Channel_ID = int(os.environ.get("ARCHIVE_CHANNEL_ID"))
    Start_Message = os.environ.get("Start_Message")
    Bot_Channel = os.environ.get("Bot_Channel_UserName")
    if Bot_Channel and Bot_Channel.startswith("@"):
        Bot_Channel = Bot_Channel[1:]
    elif Bot_Channel == "":
        Bot_Channel = None

    Link_Root = f"https://{App_Name}.herokuapp.com/"
    Download_Folder = "Files"
    Dev_Channel = "Wachu985"
    Bot_UserName = None  # The bot will set it after starting
    Part_size = 10 * 1024 * 1024  # (10MB) For Pyrogram
    Buffer_Size = 512 * 1024  # For Quart
    Pre_Dl = 3  # How many parts to download from telegram before client request them
    Separate_Time = 4  # (seconds)  wait time between messages if user send more than one
    Sleep_Threshold = 60  # (Seconds) sleep threshold for flood wait exceptions
    Max_Fast_Processes = 1  # How many links user can update them to fast links at the same time


class Strings:
    start = Config.Start_Message
    dl_link = "🔗 Enlace de Descarga"
    st_link = "🎞 Enlace Online"
    generating_link = "**⏳ Generando Enlace...**"
    bot_channel = "📢 Canal del Bot"
    dev_channel = "🤖 Desarrollador"
    fast = "⚡️**El Enlace ha sido a actualiado a Enlace Rápido**"
    update_link = "⚡ Actualizar a Enlace Rápido"
    update_limited = (f"⛔ You can update just {Config.Max_Fast_Processes} link in one time, "
                      "please wait until previous update to complete")
    re_update_link = "🔄 Volviendo a actualizar el Enlace"
    already_updated = "Este enlace ha sido Actualiado"
    wait_update = "⏳ Actualizando en Enlace.."
    wait = "⏳ Por Favor Espere..."
    progress = "⏳ Procesando"
    file_not_found = "⚠️Archivo no Encontrado, Por favor Renvie e intente de Nuevo"
    delete_manually_button = "⚠️Usted ha Eliminado esto"
    delete_forbidden = "The bot can't delete messages older than 48 hours, you can delete this message manually"
    force_join = "⚠ Unete al Canal del Bot para poder Usarlo"
