from .ninjemail_manager import Ninjemail

# Replace "YOUR_API_KEY", "USERNAME" and "TOKEN" with your actual keys
ninja = Ninjemail(
    		browser="undetected-chrome",
    		captcha_keys={"capsolver": "CAP-484787CB1A1AA5E90B97306FD43F84FC"},
    		sms_keys={"getsmscode": {"user": "mr.assesin2020@gmail.com", "token": "TOKEN"}},
			auto_proxy=True)
email, password = ninja.create_outlook_account(
    					username="testuser", 
    					password="testpassword", 
    					first_name="John", 
    					last_name="Doe", 
    					country="USA", 
    					birthdate="01-01-1990"
)

print(f"Email: {email}")
print(f"Password: {password}")
