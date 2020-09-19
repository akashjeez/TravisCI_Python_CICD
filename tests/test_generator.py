from buzz import generator
import unittest


def test_sample_single_word() -> bool:
	dataset = ('foo', 'bar', 'foobar')
	word = generator.sample(data = dataset)
	assert word in dataset


def test_sample_multiple_words() -> bool:
	dataset = ('foo', 'bar', 'foobar')
	words = generator.sample(data = dataset, limit = 2)
	assert len(words) == 2
	assert words[0] in dataset
	assert words[1] in dataset
	assert words[0] is not words[1]


def test_generate_buzz_of_atleast_5words() -> bool:
	phrase = generator.generate_buzz()
	assert len(phrase.split()) >= 5
