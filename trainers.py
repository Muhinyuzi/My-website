from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database import Trainer, Base, TrainerProfile
 
engine = create_engine('sqlite:///trainers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



#Menu for UrbanBurger
trainer1 = Trainer(name = "The Rock")

session.add(trainer1)
session.commit()

trainerProfile1 = TrainerProfile(name = "The Rock", description = "Juicy grilled veggie patty with tomato mayo and lettuce", price = "$7.50", course = "Entree", trainer = trainer1)

session.add(trainerProfile1)
session.commit()






#Menu for Super Stir Fry
trainer2 = Trainer(name = "Norbert")

session.add(trainer2)
session.commit()


TrainerProfile2 = TrainerProfile(name = "Norbert", description = "With your choice of noodles vegetables and sauces", price = "$7.99", course = "Entree", trainer = trainer2)

session.add(trainerProfile1)
session.commit()




print ("added Trainers!")
