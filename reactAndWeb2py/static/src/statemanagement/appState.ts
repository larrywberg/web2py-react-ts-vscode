import { useState, useMemo, } from 'react'

const initializeAppState = () => {
    const initialState = { 
        // HERE IS WHERE YOU DEFINE YOUR STATE VARIABLES
        count: 0,

        // The api component pieces use these to load json from a RESTful service
        apiTest_entryNext: 1,
        apiTest_entryText: 'Click the button above to load first entry using REST call to web2py server',
    }
  
    // Build the state from the initialState using React.useState()
    const [state, setState] = useState(initialState)
  
    // Build our dictionary of action functions giving it the setState method to use in those methods. 
    // useMemo() ensures this will only get called once
    const actions = useMemo(() => getActions(setState), [setState])
  
    return { state, actions }
}

// Define actions that will be available to sub components who call getAppState.
const getActions = (setState:any) => {
    return({
        increment: () => {
            setState((state:any) => ({ ...state, count: state.count + 1 }))
        },
        decrement: () => {
            setState((state:any) => ({ ...state, count: state.count - 1 }))
        },
        setEntryText: (text: string) => {
            setState((state:any) => ({ ...state, apiTest_entryText: text }))
        },
        setEntryNext: (id: number) => {
            if (id > 3) {
                id = 1
            }
            setState((state:any) => ({ ...state, apiTest_entryNext: id }))
        }
    })
}

export {  initializeAppState }