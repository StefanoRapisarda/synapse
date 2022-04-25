import logo from './logo.svg';
import './App.css';
import './drag_comp'
import DragNote from './drag_comp';
import './model'
import { notes } from './model';

function App() {
  return (
    <div>
      <h1>A draggable note</h1>
      {notes.map(note => 
          <div key={note.id}>
            <DragNote note={note}/>
          </div>
        )
      }
    </div>
  );
}

export default App;
