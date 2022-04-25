import logo from './logo.svg';
import './App.css';
import './drag_comp'
import DragNote from './drag_comp';

function App() {
  return (
    <div>
      <h1>A draggable note</h1>
      <DragNote></DragNote>
    </div>
  );
}

export default App;
