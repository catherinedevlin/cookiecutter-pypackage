from .models.meta import Base, get_engine
from .models import MyModel


def main():
    engine = get_engine()
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    main()
