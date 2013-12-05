from conceptnet.models import Concept
dog = Concept.get('dog', 'en')
for fwd in dog.get_assertions_forward()[:20]:
    print fwd

