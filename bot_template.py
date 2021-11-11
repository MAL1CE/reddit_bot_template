# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 22:44:00 2021

in order for this script to run, you must first install PRAW. https://praw.readthedocs.io/en/stable/

@author: MAD_MAL1CE
"""

import praw
import random
import time

triggers_1 = ["word_1",
              "word_2",
              "word_3"]
                
triggers_2 = ["word_4",
              "word_5",
              "word_6"]

# Put your bot's reddit id here. It will be used in several funtions.
bot_id = "bot_id_here"

# Connecting your bot to your personal script app and logging in
reddit = praw.Reddit(client_id="client_id_here",
                     client_secret="client_secret_here",
                     user_agent="<console:BOT_TEMPLATE:1.0>",
                     username='reddit_username_here',
                     password= 'reddit_password_here')

# Begins the comment stream, scans for new comments
for comment in reddit.subreddit('subreddit_name_here').stream.comments(skip_existing=True):
    
    author_name = str(comment.author.name) # Fetch author name
    author_id = str(comment.author.id) # Fetch author id
    comment_lower = comment.body.lower() # Fetch comment body and convert to lowercase
    
    with open('ignore_list.txt', 'r')as rf: # Opens ignore_list in read only mode
    
        rf_contents = rf.read() # Reads the contents of ignore list
        
        if author_id not in rf_contents and author_id != bot_id: #Checks comment against ignore list and bot id
            
            if "!ignore" in comment_lower: # Looks for the word "ignore" in the comment and checks length of comment to prevent misfire.
                
                print("Checking for bot_id")
                
                if comment.parent().author.id == bot_id: # Checks if comment is a reply to your bot
        
                    with open('ignore_list.txt', 'a') as f: # Opens ignore list in append mode
                        
                        print("##### NEW COMMENT #####")
                        print(comment.author)
                        print(comment.author.id)    
                        print(comment.body.lower())
                        print("           ")
                        
                        # Writes Username and ID of user to the ignore list
                        f.write(author_name)
                        f.write("\n")
                        f.write(author_id)
                        f.write("\n")
                        f.write("\n")
                        
                        print(" ")
                        print("User Added to Ignore List")
                        print(" ")
                        
                        # Replies to user comment
                        comment.reply("User Added to Ignore List.")
                        
                else: # if ignore is not in response to your bot, prints a false alarm message and does not add name to ignore list
                    
                    print("##### NEW COMMENT #####")
                    print(comment.author)
                    print(comment.author.id)    
                    print(comment.body.lower())
                    print("           ")
                    
                    print("           ")
                    print("&&&& False Alarm &&&&")
                    print("           ")
                    
                
            else: # If 'ignore' not present in comment body, prceeds to checking for keywords and other bot functions
                
                # This section just prints out the comment and author information
                print("##### NEW COMMENT #####")
                print(comment.submission.title)
                print("          ")
                print(comment.author)
                print(comment.author.id)    
                print(comment.body.lower())
                print("           ")
                
                if any(word in comment_lower for word in triggers_1): #Checks for keywords in comment

                    with open('responses_1.txt', 'r', encoding='utf-8') as tf:
                        
                        quote_selection = tf.read().splitlines()
                
                        print("===== Generating Reply =====")
                        generated_reply_unadjusted = random.choice(quote_selection) # Fetch random quote from list
                        generated_reply = generated_reply_unadjusted.replace("username", author_name)
                        comment.reply(generated_reply) # Replies to comment with random quote
                        print("  ")
                        print(generated_reply) # Prints random quote from reply
                        print("  ")
                        print("===== Reply Posted ======")
                        print("  ")
                        time.sleep(60) # Cooldown in seconds
                          
                elif any(word in comment_lower for word in triggers_2): #Checks for keywords in comment
                    
                    # This function rolls a die and returns true on 1
                    roll_die = random.randint(1, 8)
                    print("Dice Roll: ", roll_die)
                    roll_die_string = str(roll_die)
                    if roll_die_string == "1":
                        
                        with open('responses_2.txt', 'r', encoding='utf-8') as tf:
                            
                            quote_selection = tf.read().splitlines()

                            print("===== Generating Reply =====")
                            generated_reply_unadjusted = random.choice(quote_selection) # Fetch random quote from list
                            generated_reply = generated_reply_unadjusted.replace("username", author_name)
                            comment.reply(generated_reply) # Replies to comment with random quote
                            print("  ")
                            print(generated_reply) # Prints random quote from reply
                            print("  ")
                            print("===== Reply Posted ======")
                            print("  ")
                            time.sleep(60) # Cooldown in seconds
                  
                    else: # on a failed die roll, the comment is ignored.
                        
                        print("  ")
                        print("Roll failed, ignoring comment")
                        print("  ")
                
                    
        else: # If user on ignore list, prints User Ignored, and does not reply to comment
            
            print("##### NEW COMMENT #####")
            print(comment.author)
            print(comment.author.id)    
            print(comment.body.lower())
            print("           ")
            
            print ("!!!!!!!! User Ignored !!!!!!!!")
