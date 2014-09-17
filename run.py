__author__ = 'Edward Pie'

from gcm import GCMServer

def main():
    authorization_key = "AIzaSyA7eN-2wlEzLh2l-ACdjGv4AtWY9q_37GU"
    server = GCMServer(authorization_key)
    #CHANGE gcm_id TO THAT OF THE DEVICE YOU'RE TARGETING
    gcm_id = "APA91bGeTGYYZUnxGZI11JSOVhTkM_mvuewi2I2ydxU8EnhvyAbxykSHhVBWFLY7vONIBeIZqF3poLCL1aO8DY_vvh_fxyVyAKXcCokWFMPCbmxeBCpUE-_Gypxwj8ZQaeSGPnWPHjKNFDGReD8-8Ar99SSWk4SavA"

    server.send_to_one(gcm_id,"Push Message","Text message from GCM, now you got served!")

    #UNCOMMENT THE FOLLOWING TO SEND TO MANY
    #gcm_ids = ["id1","id2","idn"]
    #server.send_to_many(gcm_ids,"YOUR TITLE HERE","YOUR MESSAGE HERE")

if __name__ == '__main__':
    main()
