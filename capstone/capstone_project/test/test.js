const chai = require('chai')
const expect = chai.expect
var request = require('request');

const Todo = require('../todolist')
// var newTodo = new Todo()


it('add to list', () => {
	expect(newTodo.add({store: 'store'})).to.deep.equal(['groceries', false, 123, {store: 'store'}, {store: 'store'}]) 
})

it('call the list', () => {
	expect(newTodo.list).to.deep.equal(['groceries', false, 123, {store: 'store'}]) 
})

it('search list and return true ', () => {
	expect(newTodo.search(false)).to.deep.equal(true)		
})

it('delete item from list ', () => {
	expect(newTodo.delete('groceries')).to.deep.equal([false, 123, {store: 'store'}]) 
})

it('delete first item from list ', () => {
	expect(newTodo.deleteFirst(false)).to.deep.equal([false, 123, {store: 'store'}]) 
})

it('delete last item from list ', () => {
	expect(newTodo.deleteLast({store: 'store'})).to.deep.equal(['groceries', false, 123]) 
})

beforeEach(function(){
	newTodo = new Todo(['groceries', false, 123, {store: 'store'}])
})

before(() => {
	console.log('Begin')
})

afterEach(() => {
	console.log('End')
})

after(() => {
	console.log('Completed')
})