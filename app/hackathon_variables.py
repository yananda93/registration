# HACKATHON PERSONALIZATION
import os

from django.utils import timezone

HACKATHON_NAME = 'HackCU'
# Hackathon timezone
TIME_ZONE = 'MST'
# This description will be used on the html and sharing meta tags
HACKATHON_DESCRIPTION = 'HackCU is a student organization at the University of Colorado at Boulder who brings together '\
    'people for our annual technology and design events, HackCU and Local Hack Day. ' \
    'We are the largest hackathon in the Rocky Mountain Region, and '\
    'our mission is to foster learning, designing, and building in order to turn student\'s ideas into a reality!'
# Domain where application is deployed, can be set by env variable
HACKATHON_DOMAIN = os.environ.get('DOMAIN', 'localhost:8000')
# Hackathon contact email: where should all hackers contact you. It will also be used as a sender for all emails
HACKATHON_CONTACT_EMAIL = 'contact@hackcu.org'
# Hackathon logo url, will be used on all emails
HACKATHON_LOGO_URL = 'https://my.hackupc.com/static/logo.png'

HACKATHON_OG_IMAGE = 'https://hackcu.org/img/hackcu_ogimage870x442.png'
# (OPTIONAL) Track visits on your website
# HACKATHON_GOOGLE_ANALYTICS = 'UA-69542332-2'
# (OPTIONAL) Hackathon twitter user
HACKATHON_TWITTER_ACCOUNT = 'hackcu'
# (OPTIONAL) Hackathon Facebook page
HACKATHON_FACEBOOK_PAGE = 'hackcu'
# (OPTIONAL) Issues url. Where to redirect hackers if a 500 error occurs
HACKATHON_ISSUES_URL = 'https://github.com/hackcu/backend/issues/new'
# (OPTIONAL) Theme color for chrome.
# https://developers.google.com/web/fundamentals/design-and-ux/browser-customization/#meta_theme_color_for_chrome_and_opera
HACKATHON_THEME_COLOR = '#494949'

# (OPTIONAL) Applications deadline
# HACKATHON_APP_DEADLINE = timezone.datetime(2017, 2, 24, 3, 14, tzinfo=timezone.pytz.timezone(TIME_ZONE))
# (OPTIONAL) When to arrive at the hackathon
# HACKATHON_ARRIVE = 'Registration opens at 3:00 PM and closes at 6:00 PM on Friday October 13th, ' \
#                    'the opening ceremony will be at 7:00 pm.'

# (OPTIONAL) When to arrive at the hackathon
# HACKATHON_LEAVE = 'Closing ceremony will be held on Sunday October 15th from 3:00 PM to 5:00 PM. ' \
#                   'However the projects demo fair will be held in the morning from 10:30 AM to 1 PM.'
# (OPTIONAL) Hackathon live page
# HACKATHON_LIVE_PAGE = 'https://hackcu.org/live'

# (OPTIONAL) Regex to automatically match organizers emails and set them as organizers when signing up
REGEX_HACKATHON_ORGANIZER_EMAIL = '^.*@hackcu\.org$'

# Reimbursement configuration
DEFAULT_REIMBURSEMENT = 100
DEFAULT_CURRENCY = '$'
DEFAULT_EXPIRACY_DAYS = 5

# (OPTIONAL) Slack credentials
# Highly recommended to create a separate user account to extract the token from
SLACK = {
    'team': os.environ.get('SL_TEAM', 'hackupctest'),
    # Get it here: https://api.slack.com/custom-integrations/legacy-tokens
    'token': os.environ.get('SL_TOKEN', None)
}
