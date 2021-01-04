import datetime, pytz

# Timezone can be changed to any allowed values.
current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime(" %m.%d.%Y %H:%M:%S %z")

print(current_time)
