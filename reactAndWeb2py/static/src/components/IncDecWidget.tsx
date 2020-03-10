import React from 'react'
import '../styles/index.css'
import { getAppState } from './App'

// declare const window: any

const IncDecWidget = () => {
	// getAppState gets the state and actions stored on the context in the markup
	const {state, actions} = getAppState()
	return (
		<div className="widget">
			<button className="button btn btn-default" onClick={actions.decrement}> - </button>
			<div className="counter">
				{state.count}
			</div>
			<button className="button btn btn-default" onClick={actions.increment}> + </button>
		</div>
	)
}

export default IncDecWidget