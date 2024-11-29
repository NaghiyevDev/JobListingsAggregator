from fake_useragent import UserAgent

ua = UserAgent()

def get_random_user_agent():
    """Returns a random user-agent string."""
    return ua.random
