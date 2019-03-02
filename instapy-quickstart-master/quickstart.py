""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'brokeskies'
insta_password = 'Scoobydoo2'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
  """ Activity flow """		
  # general settings		
  session.set_dont_include(["friend1", "friend2", "friend3"])		
  
  # activity		
  session.like_by_tags(["fortnite"], amount=10)
