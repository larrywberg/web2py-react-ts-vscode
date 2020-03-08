import React from 'react'
import { useContext, createContext } from 'react'
import '../styles/index.css'
import {  initializeAppState } from '../statemanagement/appState'

declare const window: any

// Use a context to pass down the state and actions to all
// sub components
const AppContext = createContext({})

// Sub-components can use this function to 
// get the state and actions from the context
export const getAppState: any = () => {
    return useContext(AppContext)
}

const App = () => {
	// Use react hooks to initialize our state and actions
	const { state, actions } = initializeAppState()

	return (
		<AppContext.Provider value={{ state, actions }}>
			<div>
				<div className="helloReact">
					<h1>Hello React and Typescript!</h1>
				</div>
				<div className="flexRowContainer">
					Two React components sharing state with hooks:
				</div>
				<div className="flexRowContainer">
					<Widget />				
				</div>				
				<div className="flexRowContainer">
					<Widget />				
				</div>
				<div className="flexRowContainer">
					<div className="propsOutput">
						<span>
							window.props:
						</span>
						<pre >{
							JSON.stringify(window.props, null, 2)
						}</pre>
					</div>
				</div>
			</div>
	  </AppContext.Provider>
	)
  }

const Widget = () => {
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

export default App
