from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_session():
	# engine = create_engine('mysql+mysqldb://root:@localhost/data stage fyp')
	engine = create_engine('mysql+mysqldb://root:@localhost/fyp_coderbuddy')
	# engine = create_engine('mysql+pymysql://root:@localhost/fyp_coderbuddy')
	conn = engine.connect()

	Session = sessionmaker(bind=engine)
	s = Session()

	return s