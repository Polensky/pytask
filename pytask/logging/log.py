import logging

log = logging.getLogger('spam_application')
log.setLevel(logging.DEBUG)

file_log = logging.FileHandler('pytask.log')
file_log.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_log.setFormatter(formatter)
log.addHandler(file_log)
