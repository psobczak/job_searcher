class JobOffer:
    """
    Represents single job offer. May differ depending on the site it comes from
    """

    def __init__(self, title, source, min_salary, max_salary, link):
        self.title = title
        self.source = source
        self.min = min_salary
        self.max = max_salary
        self.link = link

    def __repr__(self):
        return f'{self.__class__.__name__}(title={self.title!r}, source={self.source!r} min_salary={self.min!r}, max_salary={self.max!r}, link={self.link!r})'
