import { render, screen } from '@testing-library/react';
import App from './App';

test('renders OctoFit Tracker app', () => {
  render(<App />);
  const appElement = screen.getByText(/OctoFit Tracker/i);
  expect(appElement).toBeInTheDocument();
});
