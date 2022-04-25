import { Draggable } from 'drag-react';
import React from 'react';
import './drag_comp.css'

class DragNote extends React.Component {
    render() {
        return (
            <Draggable>
                <div class='note'>
                    <h3 id='title'>Title</h3>
                    <p id='text'>
                        Text text text text text text text text text  text 
                        text text text  text text text text  text text text text
                    </p>
                </div>
            </Draggable>
        )
    }
}

export default DragNote;