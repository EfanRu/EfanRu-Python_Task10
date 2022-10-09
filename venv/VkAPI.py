import requests
import Profile

access_token = 'vk1.'


def send_vk_api_request(method_name, params):
    params['access_token'] = access_token
    params['v'] = '5.131'
    resp = requests.get('https://api.vk.com/method/{method}?parameters'.format(method=method_name),
                        params=params)
    return resp.json()


def get_profiles(uid):
    return Profile.get_profile_from_resp(
            send_vk_api_request('getProfiles', {'uid': uid})
        )


def get_union_friends(source_uid, target_uid):
    return send_vk_api_request('friends.getMutual', {'source_uid': source_uid, 'target_uid': target_uid})


if __name__ == '__main__':
    result = get_union_friends('X', 'Y')
    print(result)
    # slava = get_profiles('X&')
    # tanya = get_profiles('Y')
    # print(tanya.first_name + ' ' + tanya.last_name)

