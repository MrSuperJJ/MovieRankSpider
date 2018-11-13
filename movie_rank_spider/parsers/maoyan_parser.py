def parse_movie_star(movie_star):
    stars = movie_star.strip('\n 主演：').split(',')
    return stars

def parse_movie_releasetime(movie_releasetime):
    releasetime = movie_releasetime.lstrip('上映时间')
    return releasetime

def parse_movie_score(movie_score):
    return movie_score + '分'