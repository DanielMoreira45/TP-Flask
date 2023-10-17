import yaml, os.path

Anime = yaml.safe_load(
    open(
        os.path.join(
            os.path.dirname(__file__),
            "anime.yml"
            )
        )
    )
# Pour avoir un id
i = 0
for anime in Anime:
    anime['id'] = i
    i += 1

def get_sample():
    return Anime[0:10]