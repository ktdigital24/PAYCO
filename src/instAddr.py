import requests

def send_requests(method, url, data=None, headers=None):
    try:
        response = requests.request(method, url, data=data, headers=headers)
        response.raise_for_status()
        return response
    except requests.RequestException as error:
        raise Exception(f"Request failed: {error}")

class APIEmail:
    @staticmethod
    async def get_hash(id, password):
        try:
            response = send_requests(
                "POST",
                "https://m.kuku.lu/index.php",
                data=f"action=checkLogin&confirmcode=&nopost=1&csrf_token_check=03bf6696672d77cc125c375f706cf29f&csrf_subtoken_check=9668e86da7e79582acdb9a9ccfa90945&number={id}&password={password}&syncconfirm=no",
                headers={
                    "cookie": "cookie_sessionhash=SHASH%3A3418a07bdb896f250a8f8fa173bb115e;",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8"
                }
            )
            return response.text.split("OK:SHASH:")[1]
        except Exception as error:
            raise Exception("Failed to get session hash!")

    @staticmethod
    async def get_sub_token(hash):
        try:
            response = send_requests('GET', 'https://m.kuku.lu/recv.php', headers={
                "cookie": f"cookie_csrf_token=03bf6696672d77cc125c375f706cf29f; cookie_sessionhash=SHASH%3A{hash};"
            })
            return response.text.split('"action=undelMail&nopost=1&"+GetQuery("action,num")+"&num="+encodeURIComponent(_num)+"&csrf_token_check=')[1].split('csrf_subtoken_check=')[1].split('",')[0]
        except Exception as error:
            raise Exception("Failed to get sub token!")

    @staticmethod
    async def get_random_email(hash):
        try:
            response = send_requests("POST", f"https://m.kuku.lu/index.php?action=addMailAddrByAuto&nopost=1&by_system=1&t=1728301303&csrf_token_check=03bf6696672d77cc125c375f706cf29f&recaptcha_token=&_=1728301305963",
                headers={
                    "cookie": f"cookie_csrf_token=03bf6696672d77cc125c375f706cf29f; cookie_sessionhash=SHASH%3A{hash};"
                }
            )
            if "OK" in response.text:
                return response.text.split("OK:")[1]
            raise Exception("Failed to get email!")
        except Exception as error:
            raise error

    @staticmethod
    async def get_custom_email(hash, user, domain):
        try:
            response = send_requests("POST", f"https://m.kuku.lu/index.php?action=addMailAddrByManual&nopost=1&by_system=1&t=1728301303&csrf_token_check=03bf6696672d77cc125c375f706cf29f&newdomain={domain}&newuser={user}&recaptcha_token=&_=1728301305963",
                headers={
                    "cookie": f"cookie_csrf_token=03bf6696672d77cc125c375f706cf29f; cookie_sessionhash=SHASH%3A{hash};"
                }
            )
            if "OK" in response.text:
                return response.text.split("OK:")[1]
            else:
                raise Exception("Failed to get email!")
        except Exception as error:
            raise error

    @staticmethod
    async def get_num_list(hash, subtoken, email):
        try:
            # Updated URL and parameters to match Node.js version
            response = send_requests("GET",
                f"https://m.kuku.lu/recv._ajax.php?nopost=1&csrf_token_check=6ba3be0d929c9c5ecc1c5822b0203aa2&csrf_subtoken_check={subtoken}&_=1729748941667",
                headers={
                    "cookie": f'cookie_sessionhash=SHASH%3A{hash}; cookie_filter_recv2={{"filter_mailaddr":"{email}"}}'
                }
            )
            return response.text.split('mailnumlist = "')[1].split('";')[0]
        except Exception as error:
            raise error

    @staticmethod
    async def get_message(hash, email, query, subtoken, time_out=60):
        try:
            for index in range(time_out):
                response = send_requests("GET",
                    f"https://m.kuku.lu/recv._ajax.php?nopost=1&csrf_token_check=6ba3be0d929c9c5ecc1c5822b0203aa2&csrf_subtoken_check={subtoken}&_=1729748941667",
                    headers={
                        "cookie": f'cookie_sessionhash=SHASH%3A{hash}; cookie_filter_recv2={{"filter_mailaddr":"{email}"}}'
                    }
                )
                # Updated to check for query in response text like Node.js version
                if query.lower() in response.text.lower():
                    import re
                    match = re.search(r"openMailData\('(\d+)',\s*'([a-f0-9]+)'", response.text)
                    if match:
                        return {"num": match.group(1), "key": match.group(2)}
                import time
                time.sleep(1)
            raise Exception(f"Timeout after {time_out}")
        except Exception as error:
            raise Exception(f"Failed to get message! {error}")

    @staticmethod
    async def get_element_from_message(hash, num, key, regex):
        try:
            response = send_requests("POST", "https://m.kuku.lu/smphone.app.recv.view.php",
                data={
                    "num": num,
                    "key": key,
                    "noscroll": 1
                },
                headers={
                    "cookie": f"cookie_sessionhash=SHASH%3A{hash}",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8"
                }
            )
            import re
            if isinstance(regex, str):
                regex = re.compile(regex)
            match = regex.search(response.text)
            if match:
                return match.group(1).strip()
            raise Exception("Failed to get element!")
        except Exception as error:
            raise error

    @staticmethod
    async def clear_messages(hash, email, subtoken):
        try:
            num_list = await APIEmail.get_num_list(hash, email, subtoken)
            send_requests("GET", f"https://m.kuku.lu/recv._ajax.php?action=delMailList&nopost=1&q={email}&num_list={num_list}&csrf_token_check=03bf6696672d77cc125c375f706cf29f&csrf_subtoken_check={subtoken}&_=1728298123606",
                headers={
                    "cookie": f"cookie_sessionhash=SHASH%3A{hash}"
                }
            )
        except Exception as error:
            raise Exception("Failed to delete message!")
