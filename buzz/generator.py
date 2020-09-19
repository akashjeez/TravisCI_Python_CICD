import random

buzz = ('Continous Testing', 'Continous Integration', 'Continous Deploymnent',
	'Continous Improvement', 'DevOps')

adjectives = ('Complete', 'Modern', 'Self-Service', 'Integrated', 'End-to-End')

adverbs = ('Remarkably', 'Enormously', 'Substantially', 'Significantly', 'Seriously')

verbs = ('Accelerates', 'Improves', 'Enhances', 'Revamps', 'Boosts')


def sample(data: list, limit: int = 1) -> [str, list]:
	if limit == 1:
		return random.sample(data, limit)[0]
	return random.sample(data, limit)


def generate_buzz() -> str:
	buzz_terms = sample(data = buzz, limit = 2)
	phrase = ' '.join([ 
		sample( data = adjectives ), 
		buzz_terms[0],
		sample( data = adverbs ), 
		sample( data = verbs ), 
		buzz_terms[1] 
	])
	return phrase.title()


if __name__ == '__main__':
	print( generate_buzz() )