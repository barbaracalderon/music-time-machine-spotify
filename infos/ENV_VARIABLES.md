## How to set your ENVIRONMENT VARIABLES

### This is required for the App to log into your Spotify Account.

This is how I did it:

1. My configuration: **Pycharm** (Editor) and **Windows** (OS).
2. Close Pycharm first.
3. I called the CLIENT_ID as SPOTIPY_CLIENT_ID
4. I called the CLIENT_SECRET as SPOTIPY_CLIENT_SECRET
5. I called the REDIRECT_URI as SPOTIPY_REDIRECT_URI
3. Now, set the ENVIRONMENT VARIABLES as follows:

**ON WINDOWS**
```
control panel >> system and security >> system >> advanced system settings >> tab "advanced" >> 
    environment variables >> SYSTEM VARIABLES >> clicked "New" >> now type your SPOTIPY_CLIENT_ID and its value* >>
        new >> now type your SPOTIPY_CLIENT_SECRET and its value* >> new >> 
            now type your SPOTIPY_REDIRECT_URI and its value** >> CLICK OK   

---
* Spotify gave this to you
** You gave this to Spotify
```

**ON PYCHARM**
```
if Pycharm is open, close it and open it again
---

file >> settings >> search for "environment variables" >> click "edit environment variables" >> tick the box 
"include system environment variables" >> CLICK OK
```

Done.

When you run main.py, it should take your credentials and log in just fine into Spotify to do its work.

### If it wasn't helpful...

Here are some links that could point you to a direction:

- [spotipy documentation](https://spotipy.readthedocs.io/en/2.22.0/)

- [setting your environment variables (Mac/Linux)](https://www.youtube.com/watch?v=5iWhQWVXosU)

- [setting your environment variables (Windows)](https://www.youtube.com/watch?v=IolxqkL7cD8)