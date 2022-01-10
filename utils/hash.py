from hashids import Hashids

from the_shortest_url import settings

hash_id = Hashids(salt=settings.SECRET_KEY)