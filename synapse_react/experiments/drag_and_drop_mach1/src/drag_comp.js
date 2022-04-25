import { Draggable } from 'drag-react';
import React from 'react';
import './drag_comp.css'

class DragNote extends React.Component {
    constructor(props) {
        super()
        this.topic = props.note.topic
        this.author = props.note.author
        this.text = props.note.text
        if (props.note.id === '1') {
            this.color = 'note-red';
        } else if (props.note.id === '2') {
            this.color = 'note-blue';
        } else if (props.note.id === '3') {
            this.color = 'note-green';
        } else {
            this.color = 'note-black'
        }
    }

    render() {
        return (
            <Draggable>
                <div className={this.color}>
                    <h3 id='topic'>{this.topic}</h3>
                    <p id='text'>{this.text}</p>
                    <h4 id="author"><em>{this.author}</em></h4>
                </div>
            </Draggable>
        )
    }
}

export default DragNote;