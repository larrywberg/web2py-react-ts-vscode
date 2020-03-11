import React from 'react'
import { useContext, createContext } from 'react'
import '../styles/index.css'
import {  initializeAppState } from '../statemanagement/appState'
import IncDecWidget from './IncDecWidget'
import ApiTest from './ApiTest'

declare const window: any

// Use a context to pass down the state and actions list to all
// sub components
const AppContext = createContext({})

// Sub-components can use getAppState() to 
// get the state and actions from the context like this:
//     import { getAppState } from './App'
//     const {state, actions} = getAppState()
//
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
					<div className="flexRowContainer">
					React and Typescript source files are located in static/reactsrc
					</div>
				</div>
				<div className="flexRowContainer topMargin30">
					Two React components sharing state with React Hooks for state management:
				</div>
				<div className="flexRowContainer">
					<IncDecWidget />				
				</div>				
				<div className="flexRowContainer">
					<IncDecWidget />				
				</div>
				<div className="flexRowContainer" >
					<div className="topMargin30 botMargin20">
						window.props is passed down from the web2py python controller
					</div>
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
				<div className="flexRowContainer">
					<ApiTest />				
				</div>
				<div>
					
				</div>
			</div>
	  </AppContext.Provider>
	)
  }

export default App
