$SMTPServer = "<адрес_сервера>"
$SMTPPort = <порт>
$Username = "<ваш_адрес_электронной_почты>"
$Password = "<ваш_пароль>"
$From = "<ваш_адрес_электронной_почты>"
$To = "<адрес_получателя>"
$Subject = "<тема_письма>"
$Body = "<текст_письма>"

$SMTPClient = New-Object System.Net.Mail.SmtpClient($SMTPServer, $SMTPPort)
$SMTPClient.EnableSsl = $true
$SMTPClient.Credentials = New-Object System.Net.NetworkCredential($Username, $Password)

$MailMessage = New-Object System.Net.Mail.MailMessage($From, $To)
$MailMessage.Subject = $Subject
$MailMessage.Body = $Body

$SMTPClient.Send($MailMessage)