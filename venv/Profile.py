def get_profile_from_resp(response):
    data = response['response'][0]
    return Profile(data['id'], data['first_name'], data['last_name'], data['can_access_closed'], data['is_closed'])


class Profile:
    def __init__(self, profile_id, first_name, last_name, can_access_closed, is_closed):
        self.id = profile_id
        self.first_name = first_name
        self.last_name = last_name
        self.can_access_closed = can_access_closed
        self.is_closed = is_closed

