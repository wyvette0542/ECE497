// #!/usr/bin/env java

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

/**
 * 
 * @author Shuyue (Yvette) Weng
 *
 */
public class EtchMain {

	public static void main(String[] args) {
		String rowString = JOptionPane.showInputDialog("How many rows would you like?");
		int numberOfRow = Integer.parseInt(rowString);
		String columnString = JOptionPane.showInputDialog("How many columns would you like?");
		int numberOfColumn = Integer.parseInt(columnString);
		JFrame myFrame = new JFrame();
		JPanel buttons = new JPanel();
		initialize(numberOfRow, numberOfColumn, myFrame, buttons);
		
		// Create a new panel with the two control buttons
		JPanel controls = new JPanel();
		JButton newGame = new JButton("New Game");
		JButton quit = new JButton("Quit");
		JLabel instruction = new JLabel("Arrow keys for movements, 'd' for toggling delete mode.");
		controls.add(instruction);
		controls.add(newGame);
		controls.add(quit);
		myFrame.add(controls, BorderLayout.SOUTH);

		// Add listeners to each control button
		ButtonListener newGameListener = new ButtonListener(numberOfRow, numberOfColumn, newGame, myFrame, buttons);
		newGame.addMouseListener(newGameListener);
		ButtonListener quitListener = new ButtonListener(numberOfRow, numberOfColumn, quit, myFrame, buttons);
		quit.addMouseListener(quitListener);
		
		myFrame.pack();
		myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		myFrame.setVisible(true);
	}

	static void initialize(int numberOfRow, int numberOfColumn, JFrame myFrame, JPanel buttons) {
		buttons.removeAll();
		myFrame.setTitle("Etch-a-sketch");
		JButton[][] buttonList = new JButton[numberOfRow][numberOfColumn];
		// Create a new panel with all the grids. I use buttons because its the only one I remember. Don't need to click on any of it.
		JButton newButton = null;
		GridLayout layout = new GridLayout(numberOfRow, numberOfColumn);
		buttons.setLayout(layout);
		for (int i = 0; i < numberOfRow; i++) {
			for (int j = 0; j < numberOfColumn; j++) {
				if (i == 0 && j == 0) {
					newButton = new JButton("X");
				} else {
					newButton = new JButton(" ");
				}
				buttons.add(newButton);
				buttonList[i][j] = newButton;
			}
		}
		buttons.revalidate();
		myFrame.add(buttons, BorderLayout.NORTH);
		//Add KeyListener
		ArrowKeyListener keyListener = new ArrowKeyListener(numberOfRow, numberOfColumn, buttonList, myFrame);
		buttons.addKeyListener(keyListener);
		buttons.setFocusable(true);
        buttons.requestFocusInWindow();
	}

}
