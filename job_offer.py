class JobOffer:
    """
    Represents single job offer. May differ depending on the site it comes from
    """

    def __init__(self, title, min_salary, max_salary, link):
        self.title = title
        self.min = min_salary
        self.max = max_salary
        self.link = link

    def __repr__(self):
        return f'{self.__class__.__name__}(title={self.title}, min_salary={self.min}, max_salary={self.max}, link={self.link})'
