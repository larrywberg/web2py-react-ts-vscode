import { useState, useMemo, } from 'react'

const initializeAppState = () => {
    // HERE IS WHERE YOU DEFINE YOUR STATE VARIABLES
    const initialState = { 
        count: 0 
    }
  
    // Manage the state using React.useState()
    const [state, setState] = useState(initialState)
  
    // Build our actions. useMemo() as an optimization to
    // make sure this will only ever be called once.
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
        }
    })
}

export {  initializeAppState }