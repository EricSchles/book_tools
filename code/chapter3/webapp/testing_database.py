from app.server import Store

store = Store.query.all()[0] #get any old object.
print store.name
print store.email
