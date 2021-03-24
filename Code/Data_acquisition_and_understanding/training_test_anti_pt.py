import os
import urllib.request
import json
from geopy.geocoders import Nominatim
from deepface import DeepFace


path_raw_data = "../../Data/Raw/tweets_anti_pt.jsonl"
path_img_data = "../../Data/Raw/Profile_imgs_anti_pt/"
path_out_data = "../../Data/Processed/train_test_anti_pt.json"

#Init geolocator
geolocator = Nominatim(user_agent="test")

tweets = []
with open(path_raw_data, 'r') as infile:
    with open(path_out_data, 'w') as outfile:
        for i, line in enumerate(infile):
            tweet_in = json.loads(line)

            tweet = {}
            tweet["tweet_class"] = "anti-vaccine"
            tweet["creation_date"] = str(tweet_in["created_at"])
            tweet["tweet_id"] = str(tweet_in["id"])
            tweet["tweet_full_text"] = str(tweet_in["full_text"])
            tweet["user_id"] = str(tweet_in["user"]["id"])
            
            # Continue tweet processing only if it's user ID hasn't appeared before, avoids repeated users
            
            add_tweet = True
            
            for t in tweets:
                if t["user_id"] == tweet["user_id"]:
                	add_tweet = False
                	break
            
            if add_tweet:
                tweet["user_location"] = str(tweet_in["user"]["location"])
            
                tweet["user_location_normalized"] = {}
            
                # Get normalized location
                try:
                    location_normalized = geolocator.geocode(tweet["user_location"])
                except:
                    location_normalized = None
                
                # Check if a location was found
                if location_normalized is not None:
                    tweet["user_location_normalized"] = location_normalized.raw
            
                tweet["usert_description"] = str(tweet_in["user"]["description"])
                tweet["user_image_url"] = str(tweet_in["user"]["profile_image_url"])
            
                # Classify Gender and Age

                # Download and save image as a temp file
                tweet_in["user"]["profile_image_url"] = tweet_in["user"]["profile_image_url"].replace("_normal", "")
                filename, file_extension = os.path.splitext(tweet_in["user"]["profile_image_url"])
                _my_img_path = path_img_data + tweet_in["user"]["id_str"] + file_extension
            
                # Predict age, gender and race
                try:
                    urllib.request.urlretrieve(tweet_in["user"]["profile_image_url"], _my_img_path)
                    face_predict = DeepFace.analyze(img_path = _my_img_path, actions = ['age', 'gender', 'race'])
                except:
                    face_predict = {}
            
                tweet["face_predict"] = face_predict
            
                tweets.append(tweet)
      
        json.dump(tweets, outfile)


