import datetime
import time

def getDateFromString(dateTime, inputFormat, outputFormat):
  """
  This function parses date/time using inputFormat and returns date/time in outputFormat
  :param dateTime:
  :param inputFormat:
  :param outputFormat:
  :return: formattedDateTime
  """
  parsedDateTime = datetime.datetime.strptime(dateTime, inputFormat)
  formattedDateTime = datetime.datetime.strftime(parsedDateTime, outputFormat)
  
  return formattedDateTime


def getCurrentDateTime():
  """
  This function returns current date time (E.g. 2021-07-13 17:30:00.000000)
  """
  return datetime.datetime.now()


def find_last_business_date(dt):
  """
  This function converts given date (YYYYmmdd) to last business date
  """
  curr_dt = datetime.datetime.strptime(dt, '%Y%m%d')
  
  if curr_dt.weekday() == 0:  # 0=Monday
    last_business_dt = curr_dt - datetime.timedelta(days=3)
  elif curr_dt.weekday() == 6: # 6=Sunday
    last_business_dt = curr_dt - datetime.timedelta(days=2)
  else:
    last_business_dt = curr_dt - datetime.timedelta(days=1)
  
  return last_business_dt.strftime('%Y%m%d')
  
  
  def concat_curr_time(from_dt, to_dt):
    """
    This function returns the given dates with current time appended with formatting changes. E.g. from_dt = 20210713; from_dt_time = 2021-07-13 17:30:00
    """
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    from_dt_time = datetime.datetime.strptime(from_dt, '%Y%m%d').strftime("%Y-%m-%d") + " " + curr_time
    to_dt_time = datetime.datetime.strptime(to_dt, '%Y%m%d').strftime("%Y-%m-%d") + " " + curr_time
    
    return from_dt_time, to_dt_time
  
  
  def concat_start_end_day_time(dt):
    """
    This function returns the given date with the time range for entire day. E.g. dt = 20210713; from_dt_time = 2021-07-13 00:00:00; to_dt_time = 2021-07-13 23:59:59
    """
    from_dt_time = datetime.datetime.strptime(dt, '%Y%m%d').strftime("%Y-%m-%d 00:00:00")
    to_dt_time = datetime.datetime.strptime(dt, '%Y%m%d').strftime("%Y-%m-%d 23:59:59")
    
    return from_dt_time, to_dt_time
    
