
from repository.Repository import Repository
from service.Service import Service
r = Repository('data/hardE.txt', 'coord')
s = Service()
s.generate(1500,200,r.getGraph().getMatrix(),r)
