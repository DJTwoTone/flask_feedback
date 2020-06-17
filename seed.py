from models import db, User, Feedback
from app import app

db.drop_all()
db.create_all()

Feedback.query.delete()
User.query.delete()

bob = User.register(username='slowco', password='dragonballs', email='test@test.com', first_name='Doug', last_name='Blake')


harry = User.register(username='funnyguy', password='hahahahahaha', email='laugh@teehee.com', first_name='Frank', last_name='Grishham')


maggie = User.register(username='chocochippy', password='numnumnum', email='me@hungry.com', first_name='Margret', last_name='Chase')

db.session.add(bob)
db.session.add(harry)
db.session.add(maggie)

db.session.commit()

f1 = Feedback(title='test feedback 1', content='Duis sit amet sem suscipit, viverra ligula quis, faucibus tortor. Donec non sem dui. In rhoncus ultricies nunc vel porttitor.', user='slowco')
f2 = Feedback(title='test feedback 2', content='Duis sit amet sem suscipit, viverra ligula quis, faucibus tortor. Donec non sem dui. In rhoncus ultricies nunc vel porttitor.', user='slowco')
f3 = Feedback(title='test feedback 3', content='Duis sit amet sem suscipit, viverra ligula quis, faucibus tortor. Donec non sem dui. In rhoncus ultricies nunc vel porttitor.', user='funnyguy')
f4 = Feedback(title='test feedback 4', content='Duis sit amet sem suscipit, viverra ligula quis, faucibus tortor. Donec non sem dui. In rhoncus ultricies nunc vel porttitor.', user='funnyguy')
f5 = Feedback(title='test feedback 5', content='Duis sit amet sem suscipit, viverra ligula quis, faucibus tortor. Donec non sem dui. In rhoncus ultricies nunc vel porttitor.', user='chocochippy')
f6 = Feedback(title='test feedback 6', content='Duis sit amet sem suscipit, viverra ligula quis, faucibus tortor. Donec non sem dui. In rhoncus ultricies nunc vel porttitor.', user='chocochippy')


db.session.add(f1)
db.session.add(f2)
db.session.add(f3)
db.session.add(f4)
db.session.add(f5)
db.session.add(f6)

db.session.commit()