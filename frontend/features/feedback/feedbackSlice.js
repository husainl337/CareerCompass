import { createSlice } from '@reduxjs/toolkit'

// Initial state
const initialState = {
    sentiment: null,
}

export const feedbackSlice = createSlice({
    name: 'feedback',
    initialState,
    reducers: {
        feedbackState:(state,action) => {
            state.sentiment = action.payload;
        }
    }
})


export const {feedbackState} = feedbackSlice.actions;

export default feedbackSlice.reducer;