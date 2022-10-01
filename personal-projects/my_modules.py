import requests, time, os, shutil

path = os.getcwd()

total, used, free = shutil.disk_usage(path)
# Disk usage statistics
# about the given path

total_2_dp = round(total / 2**30, 2)
used_2_dp = round(used / 2**30, 2)
free_2_dp = round(free / 2**30, 2)
# round to 2 decimal points

def dfcleanup():

    timestamp = os.path.getmtime(path)
    # return last modified time of file

    days = 40

    s_in_days = time.time() - (days * 24 * 60 * 60) 
    # time.time() is current time relative to epoch => Jan 1st 1970 00:00:00 UTC
    # minus 40 days in seconds

    for file in os.listdir(path):
        #ignore the following: (.os, .exe)
        filename = os.fsdecode(file)
        
        if timestamp >= s_in_days:
            os.remove(filename)

            break

def clean_up_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxbc348834299148cda800650e65554426.mailgun.org/messages",
        auth=("api", "YOUR_API_KEY"),
        data={"from": "User <mailgun@YOUR_DOMAIN_NAME>",
            "to": ["something@example.com", "YOU@YOUR_DOMAIN_NAME"],
            "subject": "Disk clean-up complete",
            "text": (f"Disk Usage:\nTotal: {total_2_dp} GiB, Used: {used_2_dp} GiB, Free: {free_2_dp} GiB")})
