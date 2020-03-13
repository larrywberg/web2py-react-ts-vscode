import React from 'react'
import '../styles/index.css'
import { getAppState } from './App'

const ApiTest = () => {
	// getAppState gets the state and dictionary of actions stored on the context
    const {state, actions} = getAppState()
    
    const callGetEntryAPI = () => {
		// Call the REST API provided by the web2py server
		const baseUrl = "http://127.0.0.1:8000/reactAndWeb2py/api/v1/entries/"
		let fetchUrl = baseUrl + state.apiTest_entryNext + ".json"
		
		fetch(fetchUrl)
		.then(res => res.json())
		.then(
		  (result) => {
			actions.setEntryText(JSON.stringify(result.entries, null, 2))
			actions.setEntryNext(state.apiTest_entryNext+1)
		  },
		  (error) => {
			  console.log(error)
		  }
		)

    }
	
	const entryText:string = state.apiTest_entryText
	return (
		<div className="apitest">
			<div className="flexRowContainer">
				<button className="button btn btn-default" onClick={callGetEntryAPI} >
					Fetch Entry {state.apiTest_entryNext}
				</button>
			</div>
			<div className="propsOutput">
				<pre>
					{entryText}
				</pre>
			</div>

		</div>
	)
}

export default ApiTest