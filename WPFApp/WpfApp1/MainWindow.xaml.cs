using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfApp1
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void DrawTriangle(object sender, RoutedEventArgs e)
        {
            if (string.IsNullOrEmpty(point1XTB.Text) || string.IsNullOrEmpty(point1YTB.Text) ||
                string.IsNullOrEmpty(point2XTB.Text) || string.IsNullOrEmpty(point2YTB.Text) ||
                string.IsNullOrEmpty(point3XTB.Text) || string.IsNullOrEmpty(point3YTB.Text))
            {
                MessageBox.Show("Введите координаты всех трех точек для треугольника.");
                return;
            }

            Point point1, point2, point3;
            try
            {
                point1 = new Point(double.Parse(point1XTB.Text), double.Parse(point1YTB.Text));
                point2 = new Point(double.Parse(point2XTB.Text), double.Parse(point2YTB.Text));
                point3 = new Point(double.Parse(point3XTB.Text), double.Parse(point3YTB.Text));
            }
            catch (Exception ex)
            {
                MessageBox.Show("Неверный формат координат: " + ex.Message);
                return;
            }

            drawCanvas.Children.Clear();

            Polygon triangle = new Polygon();
            triangle.Points.Add(point1);
            triangle.Points.Add(point2);
            triangle.Points.Add(point3);
            triangle.Stroke = Brushes.Black;
            triangle.StrokeThickness = 2;
            triangle.Fill = Brushes.Transparent;
            drawCanvas.Children.Add(triangle);
        }
    }
    }
