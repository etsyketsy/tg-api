const masterReducer = (state = [], action) => {
    switch(action.type) {
        case 'TBD':
            return {
                ...state,
            }
        default: return state;
    };
};

export default masterReducer