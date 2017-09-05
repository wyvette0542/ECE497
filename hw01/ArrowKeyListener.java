import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JButton;
import javax.swing.JFrame;

public class ArrowKeyListener implements KeyListener{
	
	private int numberOfRow;
	private int numberOfColumn;
	private JButton[][] buttons;
	private JFrame frame;
	private int row = 0;
	private int column = 0;
	private String change = "X";
	

	public ArrowKeyListener(int numberOfRow, int numberOfColumn, JButton[][] buttonList, JFrame myFrame) {
		this.numberOfRow = numberOfRow;
		this.numberOfColumn = numberOfColumn;
		this.buttons = buttonList;
		this.frame = myFrame;
	}

	@Override
	public void keyPressed(KeyEvent e) {
		// Auto-generated method stub
		
	}

	@Override
	public void keyReleased(KeyEvent e) {
		int key = e.getKeyCode();
		if (key == KeyEvent.VK_KP_LEFT || key == KeyEvent.VK_LEFT) {
			displayChanges(0, -1);
		} else if (key == KeyEvent.VK_KP_RIGHT || key == KeyEvent.VK_RIGHT){
			displayChanges(0, 1);
		} else if (key == KeyEvent.VK_KP_UP || key == KeyEvent.VK_UP) {
			displayChanges(-1, 0);
		} else if (key == KeyEvent.VK_KP_DOWN || key == KeyEvent.VK_DOWN) {
			displayChanges(1, 0);
		} else if (e.getKeyChar() == 'd') {
			if (this.change.equals("X")) {
				this.change = " ";
			} else {
				this.change = "X";
			}
			
		}
	}

	@Override
	public void keyTyped(KeyEvent e) {
		// Auto-generated method stub
	}
	
	private void displayChanges(int x, int y){
		int newRow = x + this.row;
		int newColumn = y + this.column;
		if ((newRow < this.numberOfRow && newRow >= 0) && (newColumn < this.numberOfColumn && newColumn > -1)) {
			this.buttons[newRow][newColumn].setText(this.change);
			this.row = newRow;
			this.column = newColumn;
			this.frame.repaint();
		}
		
	}

}
